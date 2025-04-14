gitHubURL = "https://api.github.com/users/Anityasundar"

document.addEventListener('DOMContentLoaded', () => {
  console.log("Portfolio site loaded successfully!");

  const data = fetch(gitHubURL).then(res => res.json()).catch(err => console.error("Error: ", err)).finally();
  
  const githubSection = document.getElementById("github-data")
  
  if(data){

    githubSection.innerHTML = `<h2><a href="${data.html_url}">My GitHub Profile</a></h2>`
  }
});
