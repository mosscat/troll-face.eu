(function($)
{
	debugLog = function(line)
	{
		if (window.console)
			console.log(line);
	}

	browser = function()
	{
		this.name = '';
		this.version = 0;
		
		this.getBrowser = function ()
		{
			var userAgent = navigator.userAgent.toLowerCase();

			$.browser.chrome = /chrome/.test(navigator.userAgent.toLowerCase());

			// Is this a version of IE?
			if( $.browser.msie)
			{
				userAgent = $.browser.version;
				userAgent = userAgent.substring(0,userAgent.indexOf('.'));
				
				this.name = 'iexplore';
				this.version = userAgent;
			}

			// Is this a version of Chrome?
			if( $.browser.chrome)
			{
				userAgent = userAgent.substring(userAgent.indexOf('chrome/') +7);
				userAgent = userAgent.substring(0,userAgent.indexOf('.'));

				this.name = 'chrome';
				this.version = userAgent;
				// If it is chrome then jQuery thinks it's safari so we have to tell it it isn't
				$.browser.safari = false;
			}

			// Is this a version of Safari?
			if( $.browser.safari)
			{
				userAgent = userAgent.substring(userAgent.indexOf('safari/') +7);
				userAgent = userAgent.substring(0,userAgent.indexOf('.'));
				
				this.name = 'safari';
				this.version = userAgent;
			}

			// Is this a version of Mozilla?
			if( $.browser.mozilla)
			{
				this.name = 'mozilla';
				//Is it Firefox?
				if(navigator.userAgent.toLowerCase().indexOf('firefox') != -1){
					userAgent = userAgent.substring(userAgent.indexOf('firefox/') +8);
					userAgent = userAgent.substring(0,userAgent.indexOf('.'));
					this.version = userAgent;
				}
				// If not then it must be another Mozilla
				else{
				}
			}

			// Is this a version of Opera?
			if( $.browser.opera)
			{
				userAgent = userAgent.substring(userAgent.indexOf('version/') +8);
				userAgent = userAgent.substring(0,userAgent.indexOf('.'));
				
				this.name = 'opera';
				this.version = userAgent;
			}
		}

		this.getBrowser();
	}

	getCookie = function(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	// use correct width/height
    updateCenter =  function( x) {
		var pH = $(x).children().height();
		var wH = $(window).height();
		
		$(x).css({
			marginTop: ( wH - pH)/2 + 'px',
			position: 'absolute'
		});
		
        $(x).width( $(window).width());
    };

    $(document).ready( function() {
        updateCenter('#frame_0');
        updateCenter('#frame_1');

		// choose browser-orientired css
		b = new browser();
		switch( b.name)
		{
			case 'opera':
				$('head').append('<link rel="stylesheet" href="/static/css/opera.css" type="text/css" />');
				break;
			case 'mozilla':
				$('head').append('<link rel="stylesheet" href="/static/css/firefox.css" type="text/css" />');
				break;
			case 'chrome':
				$('head').append('<link rel="stylesheet" href="/static/css/chrome.css" type="text/css" />');
				break;
		}

	});
    
    $(window).resize( function() {
        updateCenter('#frame_0');
        updateCenter('#frame_1');
    });

})(jQuery);

