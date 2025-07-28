/* 
 Names: Alexia Macias, Christine Mier, Zhi Xuan Chong, Allen Le
 Start Date: July 21, 2025
 Project Name: CaZa's Library
 File Purpose: This file handles user interactions and user interface.

 TODO: implement file structure as well as layout basic features such as: navigation bar, buttons, and links
*/

document.addEventListener('DOMContentLoaded', function() {
    //button, switches, and container declarations
    const toggleSwitch = document.getElementById('toggle-members-switch');
    const membersList = document.getElementById('members-list');
    const editMembersBtn = document.getElementById('edit-members-btn');
    const closeBtn = document.querySelectorAll('.flash-close');
    const loginRedirect = document.getElementById('redirect-to-login');
    const homeRedirect = document.getElementById('redirect-to-homepage');
    const sortSelect = document.querySelector('select[name="sort-by"]');
    const searchForm = document.querySelector('form')

    //Search Page buttons
    if (sortSelect && searchForm) {
        sortSelect.addEventListener('change', () => {
            searchForm.submit();
        })
    }

    //toggle members list and edit button
    toggleSwitch.addEventListener('change', () => {
        const visible = toggleSwitch.checked;
        membersList.style.display = visible ? 'block' : 'none';

        //hide editable fields
        if (!visible) {
            document.querySelectorAll('.edit-form').forEach(form => form.style.display = 'none');
        }
    });

    //enable edit mode
    editMembersBtn.addEventListener('click', () => {
        document.querySelectorAll('.edit-form').forEach(form => {
            if (form.style.display == 'none') {
                form.style.display = 'block';
            } else {
                form.style.display = 'none';
            }
    });

    //Dismiss flash messages using close button
    closeBtn.forEach(button => {
        button.addEventListener('click', function () {
            this.parentElement.style.display = 'none';
        });
    });

    //Auto-dismiss messages after 5 seconds
    setTimeout(() => {
        const flash = document.querySelector('.flash-message');
        if (flash) {
            flash.style.display = 'none';
        }
    }, 5000);

    //redirect users to login page if user already exists
    if (loginRedirect) {
        setTimeout(() => {
            window.location.href = loginRedirect.dataset.href;
        }, 3000);
        return;
    }
    //redirect to homepage once member is created
    if (homeRedirect) {
        setTimeout(() => {
            window.location.href =  homeRedirect.dataset.href;
        }, 3000);
    }
});
});

//cancel button
function cancelEdit(btn) {
    const form = btn.closest('.edit-form');
    form.style.display = 'none';
}