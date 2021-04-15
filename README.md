
### E-Wallet
##### An online savings and loan supply management system 















------------------------------------------------------------------------------------------------------------------------------------------------------------------
#### Md. Imran Nazir - 18201071
#### Tanjina Saif Karim - 18201080
#### Department of Computer Science & Engineering
#### University of Asia Pacific
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
### PROJECT IDEA

E-Wallet is a modern software that allows users to save their money in an online platform and provide loans of any scale with less interest to eligible loan seekers. In this system registered members can save money  in their corresponding  e-wallet . The system will be able to process loan applications from registered loan seekers. The loan applications will be verified and approved by the system admin who is the superuser of this system. The approved loan requests will be forwarded to all the members and the interested members can invest a fixed amount of money in a particular loan. When the total loan amount is gathered, It is provided to the corresponding loan seeker with a fixed deadline and interest rate. When a loan seeker will repay the entire loan then the profit will be distributed among the investors according to their investments and a small percentage of profit will be allocated for the system itself. All financial services and activities will be held under the guidelines and policies of Bangladesh Bank.
OBJECTIVE
The objective of E-Wallet is to create a trusted online platform for savings and also providing loans. Loan seekers can receive loans of any scale  with less interest rate and the members can also be benefited through their investments in a loan. Banks usually do not provide loans of  small amounts and It also requires a lot of paperwork and hassle. Often It becomes difficult for people to even manage loans of small scales at any given time and the interest rates are also higher. So E-Wallet aims to solve this problem. We also want to emphasize on the importance of saving and investing money by creating a trusted financial community which will be able to create an interest in people to save money.
TARGET USERS
Any individual who is older than 17 years of age and a citizen of Bangladesh can be a user of E-Wallet . Young individuals, especially students  who intend to save money are one of  the target users of our system. Furthermore, People who want hassle free, paperless loan processing and small scale loans on a regular basis are also the target users of this system. Small financial communities, micro-economic organizations can also use this system.


### REQUIREMENT ANALYSIS
#### User Requirements

All data can be controlled and accessed upon right request.
Application has to be  easy to use and understand.
It must be able to generate reports upon request of the  user.
The system must be effective and efficient in each work process.
It has to maintain the consistency and integrity of the user data.
The system must be reliable and secure for all users.
The software should be a trusted and secure platform to save  money.
Registered users can receive loans of any scale anytime at lower interest.
The system must reduce the paperwork and hassle for loan applications.
The Transactions must happen in due time without any error.
A user friendly mobile app & website for the user's convenience.



#### System Requirements

System has to be secure for people who intend to save money and also a trusted organization that will provide loans when required.
The members and loan seekers should be able to register and login into the system.
Every user will have their individual profiles and wallets to perform their activities.
Transaction methods must be simple and easy.
Online Payment should be implemented for ease of  transactions within the system like - deposit savings, paying instalments, receiving loans etc.
Users can provide feedback as per their experience.

#### Business Requirements

System should be secure to save money and a trusted organization that will provide loans when required.
The maximum revenue should be auto distributed to the investors of the organization and a few percentages of the revenue will be taken for the system itself.
The system should be able to serve different organizations to reduce cost for developing a system like E-Wallet.
A user friendly UI is needed so that the system can have many users and the system can profit from the number of users.
The system should be able to create an interest among people to use the software.
Technology Requirements

The required Operating system for development is Linux.
The programming languages to be used are mainly Python, Django and Dart.
The platform for Frontend will be ReactJs.
The database we will be using is MySQL.
The IDE for development and implementation of project will be PyCharm
The mobile technology is native for cross platform
The Version Control System is Git (Github).
The deployment environment to be used is  Docker.

### DIAGRAMS
1. UML Use Case Diagram
System : The Scope of the system is defined by the rectangle.
Actors : There are three actors in this system,
Admin : The admin is the superuser of this system who monitors and manages the whole system. The admin is the secondary actor in this system .
Member : A member is a person who is registered in the system and intends to save and invest money.
 Loan seeker : A loan seeker is a person who is registered in this system and he/she can apply for loans and receive  loans from the system.
Member and Loan seeker both are primary actors of this system who initiate the use of the system.
Use cases : In this system, the use cases are,
Registration - Members , loan seekers and admin have association with this use case. Members and loan seekers can register to the system and they can sometimes login and also cancel registration. Hence It has an extend relationship with Registration.
Deposit - The member will deposit their savings amount and the loan seekers will deposit their instalments. So both actors have an association with this use case.
View Transaction History - All actors can view their individual transaction history and the admin can view the whole history.
Online Verification and Online Application - The admin can verify the users after registration is done and also review and approve or reject loan applications.
Payment - The loan seeker can repay his instalments through online banking and even bKash . Hence both of these have an extend relationship with Payment use case.
The diagram is shown below,

2. UML Class Diagram
Class - The individual rectangles are known as classes and each class contains It’s individual attributes and methods. 
User is an abstract class  which is the parent class for Member, Loan_Seeker and Admin class. Hence they have an inheritance relationship with the User class which is shown by an arrow sign towards User.
A member can also be a loan seeker hence the relationship between Member and Loan_seeker is denoted by an hollow diamond which is called aggregation.
The Members_wallet has a composition relationship with the Member class. It means that the Members_wallet class cannot exist without the Member class. So a wallet can only exist If It has a corresponding member related to It. The same process is applicable to Loan_Seeker and Loan_Seekers_Wallet class.
Transaction class has an association with the Member, Loan_Seeker and Admin class also. All actors can view their individual transaction history and the admin can view the whole history.
Instalment class is for the loan seekers who will repay their loans in installments. Hence It has an association with the Loan_seekers_Wallet class.
Central_Wallet class is for the loan processings and also provides the information regarding each loan. Hence It has an association with Loan_seekers_wallet, Loan_Log and Admin too.
Loan_Log class is for the members who have invested in a loan. It provides all the information regarding the members , So It has an association with the Members_wallet class and also the Central_wallet class.
The UML Class Diagram is given below,


3. Entity Relationship Diagram
Entity Relationship Diagram or ER Diagram consists of the individual entities in a system and the relationship among them. The ER Diagram of E-Wallet is described below,
Member is a base table for all the registered members. The relationship between Member and Members wallet is one to one relationship because a member can only have one wallet.
Loan seeker is also a base table for all the registered loan seekers. The relationship between Loan seeker and Loan seekers wallet is one to one relationship because an individual loan seeker can only have one wallet.
Transaction table is for all the transactions happening within the system. It is like a hub for all types of transactions like - deposit savings amount, repay loan ,pay installments, receive loan etc. So It has a one to many relationship with both Loan seekers wallet and Members wallet.
Instalment table is for the loan seekers who will repay their loans in installments. It contains all the information about a loan seekers installments regarding a specific loan. Hence It has an one to many relationship with the Loan_seekers_Wallet class.
Central_Wallet table is for the loan processings and also provides the information regarding each loan. Hence It has an association with Loan_seekers_wallet, Loan_Log and Admin too. All the relationships are one to many relationships.
Loan_Log table is for the members who have invested in a loan. It provides all the information regarding the members , So It has an one to many relationship with the Members_wallet and also the Central_wallet.
The ER Diagram is given below,


4. Data Flow Diagram (Level 0)
It is also known as a context diagram. It’s designed to be an abstract view, showing the system as a single process with its relationship to external entities. 
It represents the entire system as a single bubble with input and output data indicated by incoming/outgoing arrows. 
Here, E-wallet denotes the whole system,
 Loan Seeker has multiple inputs to the system and a loan seeker can apply for loan and pay installments to E-Wallet and E-Wallet disburse money to the loan seeker.
 Admin can process application data and take verification requests from E-Wallet. 
Members can save their money to E-Wallet and receive profit whenever a loan is repaid from the loan seeker.

5. Data Flow Diagram (Level 1)
In 1-level DFD, the context diagram is decomposed into multiple bubbles/processes. At this level, we highlight the main functions of the system and break down the high-level process of 0-level DFD into subprocesses.
 A loan seeker can apply for a loan through E-Wallet. The system is monitored by the admin If everything is alright or not,If then E-Wallet will disburse the loan amount to the loan seeker from the central wallet.The data is kept in the transaction table.
 A loan seeker can raise reports and other stuff. All data is processed by the E-Wallet storage.
 Members can save or invest money to eWallet and eWallet back money with profit after completing a certain period. A member can raise a refund request to eWallet and eWallet sends a notification to admin for approval, after the approval central wallet sends money to the eWallet gateway, and after verification, money has been refunded to the member wallet.


### DEVELOPMENT METHODOLOGY
Iterative Waterfall Model
It is one of the Base models in the Software Development Life Cycle (SDLC). It is segmented into six well defined and sequential steps. This model is simple and easy to understand and also implement. Iterative model imposes a proper planning and workflow during a project. It works very well for small projects. Works best for specific or fixed requirements. But It also has some flexibility regarding the requirements during the development process. It allows feedback to previous stages except for feasibility study. We can have the freedom to update or modify the requirements and then return to the current stage. Iterative model is called the updated version of the waterfall model for the feedback option.

For the project E-Wallet , the Iterative model is most suitable.
