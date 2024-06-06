# Blood Bank Management System

## Introduction

The Blood Bank Management System is a web application designed to address the challenges faced by blood banks in managing donor and recipient information. By providing a centralized platform for donors, recipients, and administrators, the system aims to improve the efficiency and effectiveness of blood bank operations.

## Functionality

- **Donor Registration**: Donors can register by providing their personal information, including name, date of birth, blood group, contact details, and last donation date.
- **Recipient Registration**: Recipients can register by providing their personal information, including name, date of birth, blood group, and contact details.
- **Login System**: Secure login system for donors, recipients, and administrators.
- **Admin Dashboard**: An admin dashboard to manage donor and recipient information, perform CRUD operations, and view registered donors and recipients.
- **Search Functionality**: Ability to search for donors and recipients based on blood group.
- **Data Validation**: Input validation to ensure the integrity of user-provided data.

## About Database Schema

These tables store information about donors and recipients, including their personal details such as name, date of birth, blood group, contact information, and login credentials. 
<br>The primary key of email ensure each record's uniqueness, and foreign key constraints can be added if needed to maintain data integrity.
<br>Additionally, there is an Admin table with email and password fields for managing both donors and recipients efficiently.

## Tech Stack

- **Framework**: Flask
- **Database**: MySQL
- **Frontend**: HTML
- **Backend**: Python
