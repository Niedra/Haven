<%inherit file="base.mako"/>
<%def name="title()">
    root
</%def>
<h2>Welcome to Haven</h2>
% if 'auth' in session:
<h4>Auth Information</h4>

<ul>
    <li><strong>Account ID:</strong> ${ session['auth']['id'] }</li>
    <li><strong>Name:</strong> <a href="/account/${ session['auth']['id'] }">${ session['auth']['name'] }</a></li>
</ul>
% else:
<p>You are not logged in.</p>
% endif
