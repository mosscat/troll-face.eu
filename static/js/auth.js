(function($)
{
	$(document).ready( function() {
		onMessageClose = function(){}

		$('#message').dialog({
			autoOpen: false,
			disabled: false,
			closeOnEscape: true,
			draggable: true,
			resizable: false,
			position: 'center',
			show: 'fade',
			hide: 'fade',
			modal: true,
			title: 'Simon says',
			buttons: {
				"Ok": function()
				{
					$(this).dialog('close');
				}
			},
			beforeClose: function( event, ui)
			{
				onMessageClose();
			}
		});
		
		$('#auth').dialog({
			autoOpen: false,
			disabled: false,
			closeOnEscape: true,
			draggable: true,
			resizable: false,
			position: 'center',
			show: 'fade',
			hide: 'fade',
			modal: true,

			width: 400,
			height: 200,

			title: 'who are you?',
			buttons: {
				"Ok": function()
				{
					$('input[name="uname"]').removeClass('ui-state-error');
					$('input[name="upass"]').removeClass('ui-state-error');

					var uname = $('input[name="uname"]').val();
					var upass = $('input[name="upass"]').val();

					var error = false;

					if( !( /^[a-zA-Z\d]{2,12}$/.test( uname)) )
					{
						$('input[name="uname"]').addClass('ui-state-error');
						error = true;
					}
					
					if( !( /^[a-zA-Z\d\!\@\#\$\%\^\&\*\[\]]{6,12}$/.test( upass)) )
					{
						$('input[name="upass"]').addClass('ui-state-error');
						error = true;
					}

					if( error)
						return;

					$('#ajax_loader').show();

					$.ajax({
						type: 'POST',
						async: true,
						url: '/login/',
						cache: false,
						timeout: 30000,
						data: {
							name:uname,
							pass:upass
						},
						beforeSend: function( xhr, settings)
						{
							xhr.setRequestHeader("X-CSRFToken", $('input[name=csrfmiddlewaretoken]').val());
						},
						success: function( msg) {
							if( msg['result']!='OK')
								$('#message').html('i dont know you, go away..');
							else
								$('#message').html('welcome, my friend..');
							onMessageClose = function() { window.location.reload(); }
						},
						error: function(){
							$('#ajax_loader').hide();
							$('#message').html('sheet happens..');
						},
						complete: function( r, s) {
							$('#ajax_loader').hide();
						}
					});

					$(this).dialog( 'close');
					$('#message').dialog('open');
				},
				"Cancel": function()
				{
					$(this).dialog( 'close');
				}
			},

			open: function( event, ui)
			{
				document.onmousedown = defaults.onmousedown;

				$('input[name="uname"]').val( '');
				$('input[name="upass"]').val( '');

				$('input[name="uname"]').removeClass('ui-state-error');
				$('input[name="upass"]').removeClass('ui-state-error');
				
				$(this).keyup(function(e){
					if (e.keyCode == 13) {
						$('.ui-dialog').find('button:first').trigger('click');
					}
				});
			},
			beforeClose: function( event, ui)
			{
				document.onmousedown = function() {return false;}
			}
		});
	});

	defaults =
	{
		onselectstart: null,
		onmouseup: null,
		onmousedown: null
	}

	var clicker =
	{
		count: 0,
		maxCount: 2,
		handler: function(){},

		timeoutId: null,

		click: function() {
			this.count++;

			if( this.timeoutId!=null)
				clearTimeout( this.timeoutId);

			this.timeoutId = setTimeout( function(){ clicker.reset() }, 500);

			if( this.count==this.maxCount)
				this.handler();
		},
		setHandler: function( h)
		{
			this.handler = h;
		},

		reset: function()
		{
			this.count = 0;
		}

	}

	dialogUpdate = function()
	{
	}

    $(document).ready( function() {
		dialogUpdate();

		defaults.onselectstart = document.onselectstart;
		document.onselectstart = function() {return false;} // ie

		defaults.onmousedown = document.onmousedown;
		document.onmousedown = function() {return false;}

		clicker.setHandler( function(){
			$('#auth').dialog('open');
		});

		defaults.onmouseup = document.onmouseup;
		document.onmouseup = function() { clicker.click(); }

		// CSRF token event
		$('html').ajaxSend( function(event, xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				// Only send the token to relative URLs i.e. locally.
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		});
	});

})(jQuery);