<!doctype html>
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7 ]> <html class="no-js ie6"> <![endif]-->
<!--[if IE 7 ]>    <html class="no-js ie7"> <![endif]-->
<!--[if IE 8 ]>    <html class="no-js ie8"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--> <html class="no-js"> <!--<![endif]-->
<head>
    <meta charset="utf-8">

    <!-- Always force latest IE rendering engine (even in intranet) & Chrome Frame
         Remove this if you use the .htaccess -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

    <title>${self.title()}</title>
    <meta name="description" content="">
    <meta name="author" content="">

    <!--  Mobile viewport optimized: j.mp/bplateviewport -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Place favicon.ico & apple-touch-icon.png in the root of your domain and delete these references -->
    <link rel="shortcut icon" href="${request.static_url('haven:static/favicon.ico')}">
    <link rel="apple-touch-icon" href="${request.static_url('haven:static/apple-touch-icon.png')}">


    <!-- CSS : implied media="all" -->
    <link rel="stylesheet" href="${request.static_url('haven:static/css/style.css')}?v=${rid}">
    <link rel="stylesheet" href="${request.static_url('haven:static/css/960.css')}?v=${rid}">
    <link rel="stylesheet" href="${request.static_url('haven:static/css/primary.css')}?v=${rid}">

    <!-- Uncomment if you are specifically targeting less enabled mobile browsers
    <link rel="stylesheet" media="handheld" href="${request.static_url('haven:static/css/handheld.css')}?v=${rid}">  -->

    <!-- All JavaScript at the bottom, except for Modernizr which enables HTML5 elements & feature detects -->
    <script src="${request.static_url('haven:static/js/libs/modernizr-1.6.min.js')}"></script>

</head>

<body lang="en" >

    <div id="topbar-container-wrapper">
    <div id="topbar-container" class="container_12">
        <!-- Empty Menu area -->
    </div>
    </div>

    <div id="header-container-wrapper">
    <div id="header-container" class="container_12">
        <header>
            <a title="Home" href="${request.application_url}"><img title="Dark Horizion" src="${request.static_url('haven:static/images/logo.png')}"></a>
        </header>
    </div>
    </div>

    <div class="clear"></div>

    <div id="midbar-container-wrapper">
    <div id="midbar-container" class="container_12">
        <nav>
            <ul>
                <li><a href="${request.application_url}">Home</a></li>
                <li><a href="${request.application_url}/account/list">Accounts List</a></li>
            </ul>
        </nav>
        <div id="midbar-userinfo">
            % if 'auth' in request.session:
                <p>Logged in as <a href="/account/${request.session['auth']['id']}">${request.session['auth']['name']}</a> (<a href="${request.application_url}/logout">Logout</a>)</p>
            % else:
                <p>You are not logged in. (<a href="${request.application_url}/login">Login</a>)</p>
            % endif
        </div>
    </div>
    </div>

    <div class="clear"></div>

    <div id="main-container" class="container_16">
        <div id="main" role="main" class="grid_12">
            ${self.body()}
        </div>

        <div id="sidebar" role="sidebar" class="grid_4">
            <div class="block">
                <h2>Navigation</h2>
                <ul>
                    <li><a href="#">Assets</a></li>
                    <li><a href="#">Games</a></li>
                </ul>
            </div>

            <div class="block">
                <h2>My Account</h2>
                <ul>
                    <li><a href="#">Messages</a></li>
                    <li><a href="#">My Account</a></li>
                    <li><a href="#">Logout</a></li>
                </ul>
            </div>
        </div>

        <div class="clear"></div>
    </div> <!--! end of #main-container -->

    <div id="footer-container" class="container_12">
        <footer class="grid_12">
            <p>&copy; Copyright 2010 William Chambers</p>
        </footer>
    </div> <!--! end of #footer-container -->

    <!-- JavaScript at the bottom for fast page loading -->

    <!-- Grab Google CDN's jQuery. fall back to local if necessary -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.js"></script>
    <script>!window.jQuery && document.write(unescape('%3Cscript src=${request.static_url('haven:static/js/libs/jquery-1.5.0.js"%3E%3C/script%3E')}'))</script>


    <!-- scripts concatenated and minified via ant build script-->
    <script src="${request.static_url('haven:static/js/plugins.js')}"></script>
    <script src="${request.static_url('haven:static/js/script.js')}"></script>
    <!-- end concatenated and minified scripts-->


    <!--[if lt IE 7 ]>
        <script src="${request.static_url('haven:static/js/libs/dd_belatedpng.js')}"></script>
        <script>DD_belatedPNG.fix('img, .png_bg'); // Fix any <img> or .png_bg bg-images. Also, please read goo.gl/mZiyb </script>
    <![endif]-->


    <!-- mathiasbynens.be/notes/async-analytics-snippet Change UA-XXXXX-X to be your site's ID -->
    <script>
      var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
      (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.async=1;
      g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
      s.parentNode.insertBefore(g,s)}(document,'script'));
    </script>

</body>
</html>
<%!
    rid = 2
%>