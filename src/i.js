// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/*
* @type {string}
*/
var prefix = 'http://www.aidansean.com/indigo/' ;

document.addEventListener('keydown',keydown   ,false) ;
document.getElementById('i_submit').addEventListener('click',go_to_page,false) ;

function keydown(e){ if(e.keyCode==13){ go_to_page ; } }
 
function go_to_page(){
  var meeting_id = document.getElementById('i_id').value ;
  chrome.tabs.create({ url: prefix + meeting_id }) ;
 }
 