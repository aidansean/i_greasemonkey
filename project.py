from project_module import project_object, image_object, link_object, challenge_object

p = project_object('i', 'i (greasemonkey)')
p.domain = 'http://www.aidansean.com/'
p.path = 'i'
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.folder_name = 'greasemonkey'
p.github_repo_name = 'i'
p.mathjax = False
p.links.append(link_object(p.domain, 'indigo/', 'indigo page'))
p.introduction = 'One of the projects I wrote was an indico uri shortening service, called <em><a hhref="http://aidansean.com/projects/?p=191">i</a></em> (or indigo, depending on how ugly "<em>i</em>" looks in context) but I wanted to go a step further.  So I write a greasemonkey script so that I could get to indico pages without even loading the main page.  This takes up very few pixels on the screen, making it much faster to get to the meeting pages.'
p.overview = '''This is a rather simple script.  It simply redirects (in a new tab) to the <em>i</em> page, which redirects to indico.'''
