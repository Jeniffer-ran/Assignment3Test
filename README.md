# Assignment3Test
[overview]
The requisition system is the program that allows staff to register staff basic information, generate staff requisitions,  Staff register the items and the price of the items. The status is determined based on the total price of the requisition. If the total exceeds a certain price, the manager decides the status whether it is approved or not. After finishing registering everything, the number of approved, unapproved, and pending items is displayed.

[Software Design Principles]
-KISS (keep it simple, stupid)
In this case, the code structure is simple and easy to understand. There are no abstractions.
 
 -DRY(don't repeat yourself)
Avoid writing the same code multiple times; just write it in one place. In this code, creating methods such as staff_info, requisition_detail,requisition_approval,respond_requisition,display_requisition, and requisition_statistic makes it easy to fix each functionality and are reused as needed.

- OPEN/CLOSED
Write code in a way that allows for adding new functionality while modifying existing code as little as possible. Modifying existing code may have bugs and errors.

- COMPOSITION > INHERITANCE 
The code uses composition instead of using inheriting, combine small components to create the functionality. it became easier to build flexible code and replace or extend functionality without breaking existing code. The structure should allow for flexible changes to approval rules in requisition_approval method.

- SINGLE RESPONSIBILITY
  It should have one responsibility/function, not to mix different concerns. For example, staff_info, display_requisition are responsible for one action (input, display)

- SEPARATION OF CONCERNS
Separate different roles into separate modules. This will make your code cleaner and easier to manage. It makes your code easy to understand, change and stable/reliable code. For example, in the code, the respond_requisition method is mixed with the manager's decision and puts the list.

[HOW TO IMPROVEMENT AND LIMITATIONS]
-Separation of Concern
Some parts in the code, multiple different actions in a method, for example, in the methods such as respond_requisition, requisition_approval, are mixed with input, process and decision that it could be difficult to manage or fix some parts when it becomes necessary. So far, the code is simple, and it would be easy to fix; however, when writing or adding complicated scenarios, it is necessary to separate each action into the methods, which allows for easy to understand and management of the code if some errors occur. (to Single Responsibility)

There are still concerns where staff input their information and their requisition, they can move on to the next step even if they do not enter their input in a specific format, which means that they could get a requisition without filling it in. For example, name, date, staff_id, they could just be empty. To prevent this, it is necessary to write exceptions deeply. 
(sample example)
if self.name == "":
  print("Error")


