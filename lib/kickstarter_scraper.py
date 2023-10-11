from bs4 import BeautifulSoup
import ipdb

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}

    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        image_link = project.select("div.project-thumbnail a img")[0]['src']
        description = project.select("p.bbcard_blurb")[0].text
        location = project.select("ul.project-meta span.location-name")[0].text
        percent_funded = project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")

        # Create a dictionary for each project and store it in the 'projects' dictionary
        projects[title] = {
            'image_link': image_link,
            'description': description,
            'location': location,
            'percent_funded': percent_funded
        }

    # Return the 'projects' dictionary
    return projects

if __name__ == "__main__":
    scraped_projects = create_project_dict()
    for title, project_data in scraped_projects.items():
        print(f"Title: {title}")
        print(f"Image Link: {project_data['image_link']}")
        print(f"Description: {project_data['description']}")
        print(f"Location: {project_data['location']}")
        print(f"Percent Funded: {project_data['percent_funded']}%\n")