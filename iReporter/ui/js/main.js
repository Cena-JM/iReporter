function functionAlert(msg, myYes) {
    var confirmBox = $("#alert");
    confirmBox.find(".message").text(msg);
    confirmBox.find(".yes").unbind().click(function() {
       confirmBox.hide();
    });
    confirmBox.find(".yes").click(myYes);
    confirmBox.show();
 }
function deleteAlert() {
   alert("Are you sure you want this entry deleted?");
}

function validateForm() {
   var usr_email = document.loginform.email.value;
   var usr_password = document.loginform.password.value;
   var email = "jabmn@ireporter.com";
   var admin_email = "admin@ireporter.com";
   var password = "password";
   if ((usr_email == email) && (usr_password == password)) {
      window.location.replace("account.html");
      return false;
   }
   else if ((usr_email == admin_email) && (usr_password == password)) {
      window.location.replace("admin.html");
      return false;
   }
   else {
      alert ("Login was unsuccessful, please check your username and password");
      return false;
   }
}