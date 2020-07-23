//This js file handles the stripe payment functionality
//in order for stripe to process the payment when checkout has been completed

$(function () {
  $("#payment-form").submit(function () {
    //Here the variables are created and populated with details
    //from the payment form so that they can be passed to stripe
    var form = this;
    var card = {
      number: $("#id_credit_card_number").val(),
      expMonth: $("#id_expiry_month").val(),
      expYear: $("#id_expiry_year").val(),
      cvc: $("#id_cvv").val(),
    };

    Stripe.createToken(card, function (status, response) {
      //If the status is ok then we submit the form
      if (status === 200) {
        $("#credit-card-errors").hide();
        $("#id_stripe_id").val(response.id);

        //This prevents the credit card details from being
        //submitted to our servers for security purposes
        $("#id_credit_card_number").removeAttr("name");
        $("#id_cvv").removeAttr("name");
        $("#id_expiry_month").removeAttr("name");
        $("#id_expiry_year").removeAttr("name");

        form.submit();
      } else {
        //if the status has an error, the error messages received from
        //stripe are displayed to the user
        $("#stripe-error-message").text(response.error.message);
        $("#credit-card-errors").show();
        $("#validate_card_btn").attr("disabled", false);
      }
    });
    return false;
  });
});
