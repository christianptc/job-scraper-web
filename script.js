
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

function load() {
    /* 
    
    REQUEST DATA FROM PYTHON API AND THAT DATA STORED IN jsonString

    */

    const jsonString = '[{"ID": 1, "Name": "Alice", "Birthday": "2000-01-01"}, {"ID": 2, "Name": "Bob", "Birthday": "1995-05-15"}]';

    const jobs = JSON.parse(jsonString);

    jobs.forEach(job => {
        let grid = document.getElementById("grid");
        let li = document.createElement("li");

        let company = "<span class=\"company\">" + job.Name + "</span>";
        let jobtitle = "<span class=\"job\">" + job.Birthday + "</span>";
        let location = "test location"
        let link = "<span class=\"link\"><a href=\"\">link</a></span>"
        let date = "<span class=\"date\">26.02.2026</span>"
        let buttons = "<span class=\"buttons\"><button class=\"add\" onclick=\"add(this)\">&plus;</button><button class=\"rmv\" onclick=\"remove(this)\">&minus;</button></span>"
        li.id = job.ID;
        li.innerHTML = company + jobtitle + location + link + date + buttons

        grid.appendChild(li);
        console.log(job.ID, job.Name, job.Birthday);
    });
}

function add(buttonElement) {
    let rowID = buttonElement.closest('li').id;
    console.log("added " + rowID);
}

function remove(buttonElement) {
    let rowID = buttonElement.closest('li').id;
    console.log("removed " + rowID);
}


function search() {
    var loader = document.getElementById("loader");

    var jobtitle = document.getElementById("job_search");
    var region = document.getElementById("region_search");
    
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

function initialize(table_id) {
    currActive = document.querySelector('.active')
    console.log(currActive)
    if (!currActive || (table_id === currActive.id)) return;

    currActive.classList.remove('active');

    let newActive = document.getElementById(table_id);
    newActive.classList.add("active");

}