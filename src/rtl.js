// NewTwitter RTL user script Modified for TwitterDeck
// version 0.3
// 2010-12-01
// Copyright (c) 2011 Guy Sheffer
// Based on work by Guy Sheffer (GuySoft): "Twitter Unicode Hashtags + RTL support" - http://userscripts.org/scripts/show/82584
// And Yehuda Bar-Nir
// and themiddleman: "runOnTweets" - http://userscripts.org/scripts/show/82719
// -- Thanks guys.
//
// Permission is hereby granted, free of charge, to any person
// obtaining a copy of this software and associated documentation
// files (the "Software"), to deal in the Software without
// restriction, including without limitation the rights to use,
// copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the
// Software is furnished to do so, subject to the following
// conditions:
// 
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
// OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
// HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
// WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
// FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
// OTHER DEALINGS IN THE SOFTWARE.
//
// ==UserScript==
// @name           TwitterDeck extentnion RTL
// @namespace      http://guysoft.wordpress.com
// @description    Adds RTL support and non-latin hash tags to New Twitter. Version 0.3
// @include        chrome-extension://*
// @include        *
// ==/UserScript==
runOnTweets();

function runOnTweets(callback) {
	document.addEventListener("DOMNodeInserted", function(e) {
		var statuses = e.target.getElementsByClassName("update");
		if (statuses != null && statuses.length > 0) {
			var isThereRTLChars=/[\u0590-\u05ff\u0600-\u06ff]/;
			var nonLatinHash=/#([^\x00-\x7F]+([_.][^\x00-\x7F]+)*)/g;
			
			for (var i = 0; i < statuses.length; i++) {
				var tweetText = statuses[i].innerHTML;
				if (isThereRTLChars.test(tweetText)) {
					statuses[i].style.direction="rtl";
					statuses[i].style.textAlign="right";
					if (nonLatinHash.test(tweetText)) {
					  /*
						statuses[i].innerHTML = tweetText.replace(nonLatinHash, '#<a href="http://twitter.com/search?q=$1" rel="hashtag" class="embed">$1</a>');
	*/
					}
				}
			}
		}
	}, true);
}
