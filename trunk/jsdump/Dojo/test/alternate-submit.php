<?php
   print "DATA RECEIVED: ";
   print "<ul>";
   foreach($_REQUEST as $key => $var){
     print "<li>".$key." = ".$var."</li>";
   }
   print "</ul>";
?>