<%inherit file="../base.mako"/>
<%def name="title()">
    Haven - View Account ${ account.id }
</%def>
<ul>
    <li><strong>Name:</strong> ${ account.name }</li>
    <li><strong>Email:</strong> ${ account.email }</li>
</ul>
