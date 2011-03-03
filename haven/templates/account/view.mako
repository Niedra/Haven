<%inherit file="../base.mako"/>
<%def name="title()">
    Haven - View Account ${ account.id }
</%def>
<ul>
    <li><strong>Name:</strong> ${ account.name }</li>
    % if 'auth' in request.session:
        <li><strong>Email:</strong> ${ account.email }</li>
    % endif
</ul>
