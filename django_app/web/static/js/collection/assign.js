var unAssignedStore = [];
document.addEventListener("DOMContentLoaded", function () {
    const allTasks = document.getElementById("all-tasks");
    const assignedTasks = document.getElementById("assigned-tasks");
    const saveConfigButton = document.getElementById("save-config");
    function sendRequest(url, data)
    {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        return fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Include the CSRF token in headers
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Something went wrong. Please try again.');
        });
    }
    // Move task to the correct list based on checkbox state
    function moveTask(taskItem, isChecked) {
        const parentList = isChecked ? assignedTasks : allTasks;

        // Avoid duplicate tasks in the list
        if (!parentList.contains(taskItem)) {
            parentList.appendChild(taskItem);
        }
    }

    // Add event listener to handle checkbox changes
    function attachCheckboxListener(taskItem) {
        const checkbox = taskItem.querySelector(".task-checkbox");

        checkbox.addEventListener("change", function () {
            moveTask(taskItem, checkbox.checked);
        });
    }

    // Initialize tasks in both lists
    function initializeTasks(list) {
        const tasks = list.querySelectorAll("li");
        tasks.forEach((taskItem) => {
            attachCheckboxListener(taskItem);
        });
    }

    // Initialize all tasks
    initializeTasks(allTasks);

    // Save configuration action
    saveConfigButton.addEventListener("click", function () {
        const uuid = document.querySelector('[name=collection]').value;
        const assignedTaskID = Array.from(assignedTasks.children).map(
            (item) => item.querySelector("input").value
        );
        console.log("Assigned Tasks:", assignedTaskID);
        sendRequest(
            "collection/assigntasks",
            {
                id: uuid,
                unAssigned: unAssignedStore,
                tasks: assignedTaskID
            }
        ).then(rs=>{
            alert("Tasks successfully assigned to the collection!");
            location.href = "/collection/"
        });
        
    });
});