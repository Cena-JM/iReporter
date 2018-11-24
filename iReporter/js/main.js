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