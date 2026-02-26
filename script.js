
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

function load(table) {
    let userId = get_userId();

    /* 
    
    REQUEST DATA FROM PYTHON API AND THAT DATA STORED IN jsonString

    */

    const jsonString = '[{"ID": 1, "Name": "Alice", "Birthday": "2000-01-01"}, {"ID": 2, "Name": "Bob", "Birthday": "1995-05-15"}]';

    const jobs = JSON.parse(jsonString);

    loader.classList.remove("active");
    jobs.forEach(job => {
        loader.classList.add("active");
        let grid = document.getElementById("grid");
        let li = document.createElement("li");

        let company = "<span class=\"company\">" + job.Name + "</span>";
        let jobtitle = "<span class=\"job\">" + job.Birthday + "</span>";
        let location = "test location"
        let link = "<span class=\"link\"><a href=\"\">link</a></span>"
        let date = "<span class=\"date\">26.02.2026</span>"
        let buttons = "<span class=\"buttons\"><button class=\"add\" onclick=\"add(this)\">&plus;</button></span>"
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

function search() {
    let loader = document.getElementById("loader");

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

function initialize(table_id) {
    currActive = document.querySelector('.active')
    console.log(currActive)
    if (!currActive || (table_id === currActive.id)) return;

    currActive.classList.remove('active');

    clear_grid();
    
    load(table_id)
    let newActive = document.getElementById(table_id);

    newActive.classList.add("active");

}

function get_userId() {
    let userId = localStorage.getItem("userId");

    if (!userId) {
        userId = crypto.randomUUID();
        localStorage.setItem("userId", userId);
    }
    console.log(userId)
    return userId;
}