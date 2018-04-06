function validateForm(emails) {
    return orderVerification() &&
           emailVerification(emails) &&
           inputVerification();
}

function orderVerification() {
    var form = document.forms["customerForm"];
    var totalItems = 0;

    for (var iterator = 1; iterator < form.length - 3; ++iterator) {
        if (form[iterator].value !== "0") {
            ++totalItems;
        }
    }

    if (totalItems === 0) {
        alert("Buy something!");
        return false;
    }

    return true;
}

function emailVerification(emails) {
    var email = document.forms["customerForm"]["email"].value;

    for (var i = 0; i < emails.length; ++i) {
        if (emails[i]["fields"]["email"] === email) {
            document.forms["customerForm"]["email"].validity = false;
            document.forms["customerForm"]["email"].className = "invalid";
            alert("This email is already in use.");
            return false;
        }
    }
    document.forms["customerForm"]["email"].validity = true;
    document.forms["customerForm"]["email"].className = "invalid";

    return true;
}

function inputVerification() {
    var email = document.forms["customerForm"]["email"].value;
    var orderName = document.forms["customerForm"]["orderName"].value;
    var returnValue = true;

    if (email === "") {
        document.forms["customerForm"]["email"].validity = false;
        document.forms["customerForm"]["email"].className = "invalid";
        returnValue = false;
    }
    else {
        document.forms["customerForm"]["email"].validity = true;
        document.forms["customerForm"]["email"].className = "valid";
    }

    if (orderName === "") {
        document.forms["customerForm"]["orderName"].validity = false;
        document.forms["customerForm"]["orderName"].className = "invalid";
        returnValue = false;
    }
    else {
        document.forms["customerForm"]["orderName"].validity = true;
        document.forms["customerForm"]["orderName"].className = "valid";
    }

    return returnValue;
}