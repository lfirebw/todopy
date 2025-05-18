document.addEventListener("DOMContentLoaded", function () {
  const todoList = document.getElementById("todo-list");
  const addTodoButton = document.getElementById("add-todo");
  const noTodosMessage = document.getElementById("no-todos");
  function toggleNoTodosMessage() {
    if (todoList.children.length === 0) {
        noTodosMessage.style.display = "block";
    } else {
        noTodosMessage.style.display = "none";
    }
  }
  function handleTaskEvents(listItem){
    const checkbox = listItem.querySelector("input[type='checkbox']")
    const deleteButton = listItem.querySelector("button")
    checkbox.addEventListener("change", function () {
      if (checkbox.checked) {
        // Move item to the bottom and apply strikethrough
        listItem.classList.add("line-through", "text-gray-400");
        todoList.appendChild(listItem);
      } else {
        // Remove strikethrough and move item back to the top
        listItem.classList.remove("line-through", "text-gray-400");
        todoList.insertBefore(listItem, todoList.firstChild);
      }
    });
    deleteButton.addEventListener("click", function () {
        const uuid = listItem.dataset.pid;
        listItem.remove();
        sendRequest(
            'task/delete',
            {
                id: uuid
            }
        )
        toggleNoTodosMessage();
    });
  }
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
  // Function to create a new to-do item
  function createTodoItem(task) {
    const listItem = document.createElement("li");
    listItem.className = "bg-white shadow-md rounded-lg p-4 flex justify-between items-center";
    
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.className = "mr-4";

    const taskText = document.createElement("span");
    taskText.className = "text-lg text-gray-700";
    taskText.textContent = task;

    const deleteButton = document.createElement("button");
    deleteButton.className = "text-sm text-red-500 hover:text-red-700";
    deleteButton.textContent = "Delete";

    listItem.appendChild(checkbox);
    listItem.appendChild(taskText);
    listItem.appendChild(deleteButton);
    handleTaskEvents(listItem)
    //send request
    sendRequest('task/create',{
      text: task,
      description: ""
    }).then(rs=>{
      console.log(rs)
      listItem.setAttribute("data-pid",rs.data)
    })
    return listItem;
  }

  // Add a new to-do item when the button is clicked
  addTodoButton.addEventListener("click", function () {
      const task = prompt("Enter your new to-do:");
      if (task) {
          const newTodo = createTodoItem(task);
          todoList.appendChild(newTodo);
          toggleNoTodosMessage();
      }
  });
  if(todoList.children.length > 0){
    todoList.querySelectorAll('li').forEach(el=>{
        handleTaskEvents(el)
    })
  }
  toggleNoTodosMessage();
});