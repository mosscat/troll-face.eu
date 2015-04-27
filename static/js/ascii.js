(function($)
{
	frameId = 0;

	$(document).ready( function() {
		getASCII();
		setInterval( function(){getASCII()}, 25000)
	});

	getASCII = function()
	{
		$('#ajax_loader').show();
		$.ajax({
			type: 'GET',
			async: true,
			url: '/ascii/',
			cache: false,
			timeout: 30000,
			success: function( msg) {
				$('#frame_'+frameId).html( msg);
				if( $.browser.mozilla)
					$('#frame_'+frameId).show();
				else
					$('#frame_'+frameId).fadeIn( 1000);

//				updateCanvas( 'frame_'+frameId);
				updateCenter( '#frame_'+frameId);

				frameId = 1 - frameId;
				if( $.browser.mozilla)
					$('#frame_'+frameId).hide();
				else
					$('#frame_'+frameId).fadeOut( 1000);
			},
			error: function(){
				$('#ajax_loader').hide();
			},
			complete: function( r, s) {
				$('#ajax_loader').hide();
			}
		});
	}

})(jQuery);
