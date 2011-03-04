<%inherit file="../base.mako"/>
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
            <td>${account.id}</td>
            <td><a href="/account/${account.id}">${account.name}</a></td>
            <td><a href="/admin/activate/${account.id}">Activate</a></td>
        </tr>
    % endfor
</table>
% else:
<p>No inactive accounts.</p>
% endif
