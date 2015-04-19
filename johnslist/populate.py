import os
from django.core.management import call_command

def populate():
    #add Users
    if os.path.exists("db.sqlite3"):
        os.remove("db.sqlite3")
    call_command('syncdb', interactive=False)
    
    for num in range(0,20):
        newuser = User.objects.create(username='user{0}'.format(num))
        newuser.set_password('asdf')
        newuser.save()

    #add Organizations
    plug = Organization.objects.create(
        name="Purdue Linux Users Group",
        admin=User.objects.get(id=1),
        description=" Linux is a free computer operating system. It runs on a large variety of computer hardware, and can be used for many purposes including desktop machines, small embedded systems and Internet servers. You can find more information about Linux itself on the Linux International website. The Linux Documentation Project is also a good place to find general information about Linux.",
        email="president@purduelug.org",
        phone_number="123-456-7890")
    plug.icon.save('plug.png', File(open(PIC_POPULATE_DIR+'plug.png')), 'r')
        

    epics = Organization.objects.create(
        name="Engineering Projects in Communitiy Service",
        admin=User.objects.get(id=1),
        description=" Community service agencies face a future in which they must take advantage of technology to improve, coordinate, account for, and deliver the services they provide. They need the help of people with strong technical backgrounds. Undergraduate students face a future in which they will need more than solid expertise in their discipline to succeed. They will be expected to work with people of many different backgrounds to identify and achieve goals. They need educational experiences that can help them broaden their skills. The challenge is to bring these two groups together in a mutually beneficial way. In response to this challenge, Purdue University has created EPICS: Engineering Projects In Community Service",
        email="epics@purdue.edu",
        phone_number="123-456-7890")
    epics.icon.save('epics.png', File(open(PIC_POPULATE_DIR+'epics.png', 'r')))

    amet = Organization.objects.create(
        name="Association of Mechanical & Electrical Technologies",
        admin=User.objects.get(id=2),
        description="The Association of Mechanical and Electrical Technologists (AMET) is an organization that brings science, technology, engineering, and mathematics (STEM)-based students together to discuss and work on various extra-curricular projects throughout the school year. The group is meant to help educate students on what it is like to be in an interdisciplinary team and have fun at the same time. Past and current projects include the following: gas grand prix, robosumo competitions, high altitude vehicle launches, a robotic assistant for people with limb paralysis, loudspeaker design / construction, and the National Rube Goldberg competition. Along with projects, AMET hosts various company sponsored lectures and recruitment efforts for our students.",
        email="ahaberly@purdue.edu",
        phone_number="123-456-7890")
    amet.icon.save('amet.png', File(open(PIC_POPULATE_DIR+'amet.png', 'r')))

    #add Users to Organizations
    users = User.objects.all().exclude(username="AnonymousUser")
    for user in users[0:6]:
        plug.members.add(user)
        epics.members.add(user)

    #add ServiceServiceCategory's
    categories=['engineering','computer science','construction','music','art','painting','linux','web development','iOS','Android']
    for category in categories:
       Category.objects.create( name=category,description='' ) 

    plug.categories.add(Category.objects.get(name="computer science"), Category.objects.get(name="linux"))
    epics.categories.add(Category.objects.get(name = 'engineering'))
    amet.categories.add(Category.objects.get(name= 'engineering'))
    
    #add Jobs
    jobs = ['Installing linux','Configuring vim','Make a website', 'Make a car', 'Finish circuit board', 'Finish software']
    user_num = 1
    org_num = 1
    acc = True

    for job in jobs:
        Job.objects.create(name=job, description = 'Description of the job', duedate = '2015-3-21', creator = User.objects.get(id = user_num))
        Job.objects.get(id = user_num).setUpJobrelation(Organization.objects.get(id = org_num), acc)
        if acc == False:
            org_num += 1
            acc = True
        else:
            acc = False
        user_num += 1

#print what object is being added, return the object
def status(added_obj):
    if added_obj[1]:
        print "Adding {0}".format(added_obj[0])
    else:
        print "<{0}> {1} already exists".format(added_obj[0].__class__.__name__,added_obj[0])
    return added_obj[0]

if __name__ == '__main__':
        
    print 'Populating database...'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'johnslist.settings')
    from django.core.files import File
    from dbtest.models import *
    from johnslist.settings import PIC_POPULATE_DIR
    from time import sleep
    import django
    django.setup()
    populate()

