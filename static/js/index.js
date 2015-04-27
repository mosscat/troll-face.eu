(function($)
{
	updateCanvas = function( id)
	{
		text = $('#'+id).html();
		w = $(window).width();
		h = $(window).height();

		$('#'+id).html( '<canvas id="output_'+id+'" width='+w+' height='+h+'></canvas>');

		render( 'output_'+id, text, w, h);
	}

	render = function( canvas, text, w, h)
	{
		var len = text.length;
		var font_size = 5;

		var ctx = document.getElementById( canvas).getContext("2d");
		ctx.clearRect(0, 0, w, h);

		ctx.font = font_size + "pt Courier";
		ctx.textAlign = "left";
		ctx.textBaseline = "top";
		
//		ctx.save();

		var x = 0, y = 0;
		
		var temp = '';
		var is_tag = true;
		for( var i = 0; i<len; i++)
		{
			if( ( text[i]=='<') && temp!=='')
			{
				if( ( /^\<pre\>$/.test(temp)) || ( /^\<\/pre\>$/.test(temp)) || ( /^\<\/font\>$/.test(temp)))
				{ debugLog( temp); temp = ''; }
				else if( /^\<br\>$/.test(temp))
				{ debugLog( temp); temp = ''; y += ( font_size-1); x = 0; }
				else if( ( col = temp.match(/^\<font color\=\"(.*)\"\>$/)))
				{ debugLog( temp); temp = ''; ctx.fillStyle = col[1]; }
				else
				{
					debugLog( x + ", " + y + ": " + temp);

					ctx.fillText( temp, x, y);
					x += temp.length * ( font_size -1);

					temp = '';
				}
			}
			
			temp += text[i];
			if( ( text[i]=='>'))
			{
				if( ( /^\<pre\>$/.test(temp)) || ( /^\<\/pre\>$/.test(temp)) || ( /^\<\/font\>$/.test(temp)))
				{ debugLog( temp); temp = ''; }
				else if( /^\<br\>$/.test(temp))
				{ debugLog( temp); temp = ''; y += ( font_size-1); x = 0; }
				else if( ( col = temp.match(/^\<font color\=\"(.*)\"\>$/)))
				{ debugLog( temp); temp = ''; ctx.fillStyle = col[1]; }
			}
		}
//		ctx.restore();

//		setTimeout( render, 10, canvas, text, w, h);
	}

})(jQuery);
