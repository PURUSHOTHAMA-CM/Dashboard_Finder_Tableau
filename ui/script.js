async function searchDashboard() {
    const query = document.getElementById("input").value;

    chat=document.getElementById("chatBox");
    chat.innerHTML+=`<div>USER: ${query}</div>`;

    try{
        const response = await fetch(`https://dashboard-finder-tableau-2.onrender.com/search?query=${query}`);
        const data = await response.json();

        console.log(data);
        data_url=`<a href="${data.url}">View</a>`;
        botReply(`Loading: ${data.name}`);
        botReply(data_url);
        // rendering dashboard
        try{
        loadDashboard(data.url);
        }
        catch(err){
            console.log("Error in loadDashboard");
        }
    }
    catch(err)
    {
        console.log(err);
        botReply("BOT: Error Loading Server");
    }
}

function loadDashboard(url) {
    const container = document.getElementById("dashboard");

    container.innerHTML = `
        <tableau-viz 
            src="${url}" 
            width="100%" 
            height="600">
        </tableau-viz>
    `;
}


function botReply(message)
{
    chat=document.getElementById("chatBox");
    chat.innerHTML+=`<div>BOT: ${message}</div>`;
}
