const url = "http://127.0.0.1:8000"

// GLOBALS

let userId = localStorage.getItem("userId");

if (!userId) {
        userId = crypto.randomUUID();
        localStorage.setItem("userId", userId);
    }

const loader = document.getElementById("loader");
const grid = document.getElementById("grid");

// GLOBALS END

function valid_input(input1, input2) {
    if (!(input1 && input1.value)) {
        console.log("input1");
        input1.classList.add("missing");
    } else {
        input1.classList.remove("missing");
    }

    if (!(input2 && input2.value)) {
        console.log("input2");
        input2.classList.add("missing");
    } else {
        input2.classList.remove("missing");
    }
    
    if (input1.value == "" || input2.value == "") return false;
    
    return true;
}

function renderJobs(jobs) {
    clear_grid();
    grid.classList.add("loading");
    loader.classList.add("active");

    setTimeout(() => {
        jobs.forEach(job => {
            let company = "<span class=\"column_left\">" + job.company + "</span>";
            let jobtitle = "<span class=\"column_left\">" + job.job_title + "</span>";
            let location = "<span class=\"column\">" + job.location + "</span>";
            let link = "<span class=\"column\"><a href=\""+ job.link +"\">LINK</a></span>";
            let date = "<span class=\"column\">" + job.date + "</span>";
            let buttons = "<span class=\"buttons\"><button class=\"add\" onclick=\"add(this)\">&plus;</button></span>";

            let li = document.createElement("li");

            li.id = job.id;
            li.innerHTML = company + jobtitle + location + link + date + buttons;

            grid.appendChild(li);
            console.log(job.ID, job.Name, job.Birthday);
        });

        grid.classList.remove("loading");
        loader.classList.remove("active");
    }, 2000);
}

function fetchJobs(table) {
    fetch(`${url}/init/${userId}/${table}`)
        .then(response => response.json())
        .then(data=> {
            console.log(data)
            renderJobs(data)
        })
        .catch(error => console.error("ERROR: ", error));
}

function add(buttonElement) {
    let rowID = buttonElement.closest('li').id;
    console.log("added " + rowID);
}

function search() {
    let jobtitle = document.getElementById("job_search");
    let region = document.getElementById("region_search");
    
    if (!valid_input(jobtitle, region)) return;

    loader.classList.add("active");
    console.log("end");
    loader.classList.remove("active");
    console.log(jobtitle.value, region.value);
}

// One line function just to make the code more readable :)
function clear_grid() {
    document.getElementById("grid").innerHTML = "";
}

function toggleTableView(table_id) {
    currActive = document.querySelector('.active');
    console.log(currActive);
    if (!currActive || (table_id === currActive.id)) return;

    currActive.classList.remove('active');

    // clears current table rows to make space for new content
    clear_grid();
    // load function will request and present saved content for the clicked tab.
    fetchJobs(table_id);

    let newActive = document.getElementById(table_id);

    newActive.classList.add("active");
}

function ping_online() {
    // send ping to database that user is online
    return
}

function repeat_ping() {
    ping_online();
    setInterval(ping_online, 60000);
}

function test() {
    console.log("test");
}

// MAIN 

fetchJobs('searched');

repeat_ping();

// MAIN END