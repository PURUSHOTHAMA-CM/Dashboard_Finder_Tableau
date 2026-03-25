function send() {
    let input = document.getElementById("input").value.toLowerCase();

    let dashboard = findDashboard(input);

    if (dashboard) {
        document.getElementById("frame").src = dashboard.url;
        addMessage(`Loaded: ${dashboard.name} \n Link: <a href=${dashboard.url} >View</a>`)
    } else {
        addMessage("No matching dashboard found ❌");
    }
}

function findDashboard(query) {
    let max_score=0;
    let matched_dash=null;

    for (let dash of dashboards) {
        let score=0;
        for (let field of dash.fields) {

            let words=field.toLowerCase().split(" ");

            for (let word of words){
            if (query.includes(word.toLowerCase())) {
                score++;
            }
            }
        }
    
        // selecting the dashboard with maximum matching
        if(score>max_score)
        {
           max_score=score;
           matched_dash=dash;
        }
    }
    // return the selected dashboard
    if(max_score>0)
    {
        return matched_dash;
    }
    

    return null;
}

function addMessage(msg) {
    let chat = document.getElementById("chatBox");
    chat.innerHTML += "<div>" + msg + "</div>";
}