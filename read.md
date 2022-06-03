get baskets belonging to a single customer
Write a function called get customer baskets that takes in the email address and the data array as arguments and returns a list/array of all the shopping baskets that belong to the customer with that email address.

If the customer has no shopping baskets then return an empty list/array.

e.g. getCustomerBaskets("tshepo@umuzi.org", dataStore);

get a list of all the customer email addresses
Write a function called get all customers, the function should take the data array as an argument and should return a list of customer email addresses. The list must have no duplicates.

e.g. getAllCustomers(dataStore);

list all the items that have been paid for but not yet delivered
Write a function called required stock, your function should take the data array as an argument and should return all the items that need to be sent out for delivery. You need to return data in the correct format. Just include the names and quantities of the items.

e.g. requiredStock(dataStore);

For example, if one customer paid for 2 hamsters and another customer paid for one hamster and a bag of sawdust then your function should return the following data structure:

[
    {"name":"hamster", "quantity": 3},
    {"name": "bag of sawdust", "quantity": 1}
]
Get the total amount spent by a customer
Write a function called total spent that takes an email address as an argument and the data array. The function must return the total amount that the customer has spent up until this time.

e.g. totalSpent("ryan@umuzi.org", dataStore);

Note that if a basket has been delivered then it has been paid for.

Top customers
Write a function called top customers that takes the data array as an argument and returns a list/array of all the customers. The result should be ordered according to the total amount spent. The returned data structure should be an array/list of dictionaries/objects showing the email addresses and the total amounts spent per customer.

e.g. topCustomers(dataStore);

Make sure the returned value matches the following structure:

[
    {"email": "tshepo@umuzi.org", "total": 1023.10},
    {"email": "maru@email.com", "total":950},
    ... etc
]
Hint: You have already defined some functions that would be useful in finding this result. Call those functions.

customers who have OPEN baskets
Write a function called get customers with open baskets that takes in the data array as an argument and returns a list/array of email addresses for customers who have baskets that are open. e.g. getCustomersWithOpenBaskets(dataStore);

