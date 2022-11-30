function getData()
{
    let browser_codeName = navigator.appCodeName;
    let browser_version = navigator.appVersion;
    let browser_language = navigator.language;
    let cookies_enabled = navigator.cookieEnabled;
    let platform = navigator.platform;
    let user_agent_header = navigator.userAgent;
    let timezone_utc = offset_to_utc()
    let timezone_place = Intl.DateTimeFormat().resolvedOptions().timeZone
    let screen_size = screen.width + "X" + screen.height
    let battery_level = battery_getter()

    const formdata = new FormData()
    // const csrf = document.getElementsByName('csrfmiddlewaretoken')
    


    // formdata.append('csrfmiddlewaretoken',csrf[0].value)
    formdata.append("browser_codeName",browser_codeName)
    formdata.append("browser_version",browser_version)
    formdata.append("browser_language",browser_language)
    formdata.append("cookies_enabled",cookies_enabled)
    formdata.append("platform",platform)
    formdata.append("user_agent_header",user_agent_header)
    formdata.append("timezone_utc",timezone_utc)
    formdata.append("timezone_place",timezone_place)
    formdata.append("screen_size",screen_size)
    formdata.append("battery_level",battery_level)
    

    
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/rec",
        enctype: 'multipart/form-data',
        data : formdata,

        cache: false,
        contentType: false,
        processData: false,
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        beforeSend: function(xhr) { xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest"); },
      });

      
}

function send(){
  getData()
}


function offset_to_utc(){
  var date = new Date();
  var offset = date.getTimezoneOffset();
  
  utc_number = (-offset)/60

  utc = "UTC " + utc_number

  return utc
}
function battery_getter(){
  level = ""
  try {
    navigator.getBattery().then(function(battery) {
      battery.addEventListener('levelchange', function() {    
        })
        level = (battery.level*100)+"%"
      });
    
  } catch (error) {
    level = "NaN!"
  }
  return level
}