# Assignment3Test
[overview]
The requisition system is the program that allow staff to register staff basic information , generate staff requisition ,  Staff register the items and the price of the items. the status is determined based on the total price of the requisition. If the total exceeds a certain price, the manager decides the status whether it is approved or non-approved. after finishing register everythin, the number of approved, unapproved, and pending items are displayed.

[Software Design Principles]
-KISS (keep it simple, stupid)


- KISS(keep it simple, stupid)
i tried most of my code to be simple and easy understand for everyone and especially me when i open the file after for while. i should have added some coments where i was struggle to solve the programing. 

- DRY(don't repreat your self)
Try not to write same code multiple times, just write it in one place. it take time to correct the code and it may leave the errors somewhere if you write same code many times. to prevent this happening, you have to make sure that not to write same code, if you want to write, you put it in one place by using some methods.

- OPEN/CLOSED
Write code in a way that allows you to add new functionality while modifying existing codes as little as possible. Modifying existing code may have bugs and errors. not changing existing code make it easy to maintain for teams/ peaples especially when you are woking on large project

- COMPOSITION > INHERITANCE
When adding functionality, instead of inheriting and adding classes, combine small components  to create the functionality. if you rely too much on inheritance , it  can be difficult to understand where is the right hierarchy also If you change a parent class, it affects all child classes , which can lead to unexpected issues. However by using composition instead of using inheritance, it become easier to build flexible code and replace or extend functionality without breaking existing code.

- SINGLE RESPONSIBILITY
  it should have one responsibility/function not to mixing defferent concers. if you assign multiple roles , there is a possibility that changes will occur for each reason. the code is clean, easy to test, and changes will have little impact.

- SEPARATION OF CONCERNS
  Separate different roles into separate modules.This will make your code cleaner and easier to manage.it make your code be easy to understand, changing and stable/reliable code.

- YAGNI(you aren't gonna need it )
  write code when you are required. Don’t write when 
  
-REFACTORING


-HOW THE CODE MEETS DESIGN PRINCIPLES
-HOW THE CODE DOESN'T MEET DESIGN PRINCIPLES
-LIMITATIONS
-SUGGESTIONs OF IMPROVEMENT

