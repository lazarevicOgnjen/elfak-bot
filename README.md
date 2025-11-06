# 📢 College Notifications Bot

> [!warning]
> **View-Only Repository:** This code is provided for inspection **only**. You **may not copy, modify, redistribute, or use** it without written permission from Ognjen Lazarević. [See the LICENSE file for details.](https://github.com/lazarevicOgnjen/elfak-bot/blob/main/LICENSE)

---

## Overview

This project is a **notification bot for college students** that automatically monitors college webpages and sends updates to students based on their selected subjects. It’s designed to help students stay informed without manually checking multiple sources.

---

## How It Works

1. **Collecting Student Preferences**  
   - Students submit their preferences through a **Google Form**.  
   - Responses are stored in a **master Google Sheet**.  
   - A Google Apps Script filters the responses and distributes them into **individual sheets**, one for each subject.

2. **Storing Emails in the Repository**  
   - Each subject has its own `.md` file containing the students’ emails.  
   - These files are used by the bot to send notifications.

3. **Monitoring College Webpages**  
   - The bot visits designated college webpages **every 30 minutes**.  
   - When a new post or update is detected:
     - A **screenshot** of the update is taken.
     - The **text content** is scraped and saved into the corresponding `.md` file.
     - A notification email is sent to all students who have subscribed to that subject.

4. **Notification Email Contents**  
   Each email includes:
   - Screenshot of the new post (for visual context)  
   - Direct link to the **exact webpage** with the new content  
   - Link to the **Google Form** if students want to update their preferences

---

## Key Features

- Automatic collection of student preferences  
- Subject-specific storage of emails  
- Automated monitoring of webpages  
- Screenshot + text capture of new updates  
- Personalized email notifications to students  
- Links for quick access and preference updates  

---

## ⚠️ Notes

- **Do not reuse, modify, or redistribute** this code without written permission.  
- This repository is **view-only**; it is meant for review and evaluation purposes.  
- Emails and other sensitive data are stored in `.md` files and should be treated confidentially.

---

## Contact

If you need permission to **use, modify, or deploy** this project, contact:

**Ognjen Lazarević**  
<lazarevic.ognjen.elfak@gmail.com>
