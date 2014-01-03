# This file is for importing data from a tracks xml export

import xml.etree.ElementTree as ET
from django.template.defaultfilters import slugify

from gtd.models import Context, Thing, Project

INPUT_FILE = 'tracks_data.xml'
INVALID_CONTEXT_NAME = 'invalid'

def create_context(name):
    if name[0] == '@':
        name = name[1:]
    slug = slugify(name)
    c = Context(name=name, slug=slug)
    c.save()

def create_project(name):
    if name[0] == '@':
        name = name[1:]
    slug = slugify(name)
    p = Project(name=name, slug=slug)
    p.save()

def create_wrapper(fcn, 
                   class_name,
                   item_name,
                   ):
    item_exists = len(class_name.objects.filter(name=item_name))
    if not item_exists:
        fcn(name=item_name,
                )
        print 'Created %s' % item_name
    else:
        pass #print '%s already existed' % item_name

def get_instance_or_none(obj_class, obj_name):
    try:
        obj = obj_class.objects.get(name=obj_name)
    except:
        obj = None
    return obj

def validate_max_length(obj_class, xml_branch, input_field_name):
    short_desc_field = 'name'
    max_description_length = max((len(t.find(input_field_name).text) 
                                  for t in xml_branch.getchildren()))
    short_desc_max_length = obj_class._meta.get_field(short_desc_field).max_length
    if max_description_length > short_desc_max_length:
        import sys
        sys.exit(('A description/name for an import object of class %s\n'+ 
                  ' exceeds field %s max length of %d' ) % (
                                     obj_class._meta.model_name,
                                     short_desc_field, 
                                     short_desc_max_length)  )
    else:
        print 'Validation passed for %s' % obj_class._meta.model_name

def name_from_dict(names_dict, str_id):
    if str_id == None:
        return ''
    try:
        name = names_dict[int(str_id)]
    except KeyError:
        name = ''
    return name

def import_all():
    print 'Executing importer.py'
    tree = ET.parse('tracks_data.xml')
    root = tree.getroot()

    # Create invalid context for later use
    create_wrapper(fcn=create_context,
                   class_name=Context,
                   item_name= INVALID_CONTEXT_NAME)

    context_names_dict = {}
    contexts_branch = root.find('contexts')
    validate_max_length(obj_class=Context, 
                        xml_branch=contexts_branch, 
                        input_field_name='name')
    for c in contexts_branch.getchildren():
        context_name = c.find('name').text 
        context_names_dict[int(c.find('id').text)] = context_name
        create_wrapper(fcn=create_context,
                       class_name=Context,
                       item_name=context_name)

    project_names_dict = {}
    projects_branch = root.find('projects')
    validate_max_length(obj_class=Project, 
                        xml_branch=projects_branch, 
                        input_field_name='name')
    for p in projects_branch.getchildren():
        project_name = p.find('name').text 
        project_names_dict[int(p.find('id').text)] = project_name
        create_wrapper(fcn=create_project,
                       class_name=Project,
                       item_name=project_name)

    todos_branch = root.find('todos')
    validate_max_length(obj_class=Thing, 
                        xml_branch=todos_branch, 
                        input_field_name='description')
    for old_todo in todos_branch.getchildren():
        old_todo_completed = old_todo.find('state').text == 'completed'
        old_todo_short_desc = old_todo.find('description').text,
        
        todo_already_exists = len(Thing.objects.filter(name=old_todo_short_desc))
        if (not old_todo_completed) and (not todo_already_exists):

            # notes first
            old_todo_notes = old_todo.find('rendered-notes').text
            if old_todo_notes == None:
                old_todo_notes = old_todo_short_desc

            # Now context/project
            old_project_name = name_from_dict(project_names_dict,
                                          old_todo.find('project-id').text)
            old_context_name = name_from_dict(context_names_dict,
                                          old_todo.find('context-id').text)
            old_thing_project = get_instance_or_none(Project, old_project_name)
            old_thing_context = get_instance_or_none(Context, old_context_name)
            if old_thing_context == None:
                old_thing_context = get_instance_or_none(Context, 
                                                         INVALID_CONTEXT_NAME)

            # Now print results (for debugging/troubleshooting)
            print "p=%s %s, c=%s %s, %s, %s, %s" % (
                old_todo.find('project-id').text,
                old_project_name,
                old_todo.find('context-id').text,
                old_context_name, 
                old_todo.find('state').text,
                old_todo_short_desc,
                old_todo_notes,
                )
            try:
                new_thing = Thing(name=old_todo_short_desc,
                                  project=old_thing_project,
                                  context=old_thing_context,
                                  description=old_todo_notes
                                  )
                new_thing.save()
            except Exception as ex:
                print str(ex)
                err_str = 'failed to create %s' % old_todo_short_desc
                print 
                import sys
                sys.exit(err_str)
        # end not old_todo_completed
    # end for old_todo in todos_branch...
    print context_names_dict # aoeu
# Create invalid context for later use

SDAY_MAYBE_CONTEXT_STR = 'sdaymaybe'
def incubate_by_context_name():
    for t in Thing.objects.all():
        if t.context.name.lower().find(SDAY_MAYBE_CONTEXT_STR) >= 0:
            t.status = t.STATE_INCUBATE
            t.save()
# end incubate_by_context_name():


INBOX_CONTEXT_STR = 'inbox'
def inbox_by_context_name():
    for t in Thing.objects.all():
        if t.context.name.lower().find(INBOX_CONTEXT_STR) >= 0:
            t.status = t.STATE_INBOX
            t.save()
# end incubate_by_context_name():
        

def main():
    import_all()
    incubate_by_context_name()

if __name__ == "__main__":
    main() 
