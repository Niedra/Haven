<%inherit file="../base.mako"/>
<%def name="title()">
    Haven - View Account 
</%def>
<ul>
    <li><strong>Name:</strong> ${ account.name }</li>
    <li><strong>Created:</strong> ${ account.date_created.strftime("%A, %d. %B %Y %I:%M%p") }</li>
    <li><strong>Last Updated:</strong> ${ account.date_updated.strftime("%A, %d. %B %Y %I:%M%p") }</li>
    <li><strong>Status:</strong>
        % if account.activated:
            Active
        % else:
            Not Active
        % endif
    </li>
    % if 'auth' in request.session:
        <li><strong>Email:</strong> ${ account.email }</li>
    % endif
</ul>
