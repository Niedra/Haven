<%inherit file="../base.mako"/>
<%import uuid %>
<%def name="title()">
    Haven - Activate Accounts
</%def>
<h2>Activate Accounts</h2>

% if accounts:
<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Activate</th>
    </tr>
    % for account in accounts:
        <tr>
            <td>${uuid.UUID(bytes=account.id)}</td>
            <td><a href="/account/${uuid.UUID(bytes=account.id)}">${account.name}</a></td>
            <td><a href="/admin/activate/${uuid.UUID(bytes=account.id)}">Activate</a></td>
        </tr>
    % endfor
</table>
% else:
<p>No inactive accounts.</p>
% endif
