$('#update_profile').submit(function(event) {
    event.preventDefault();
    var formData = $(this).serialize();
    $.ajax({
        type: 'POST',
        url: '/profile_page',
        data: formData,
        success: function(response) {
            alert('Profile updated successfully!');
        },
        error: function(xhr, status, error) {
            alert('Error updating profile: ' + error);
        }
        });
    });
