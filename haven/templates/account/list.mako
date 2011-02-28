<%inherit file="../base.mako"/>

<%def name="title()">
    Haven - Accounts List
</%def>

<h2>Accounts List</h2>

% if accounts:
<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
    </tr>
    % for account in accounts:
        <tr>
            <td>${account.id}</td>
            <td><a href="/account/${account.id}">${account.name}</a></td>
        </tr>
    % endfor
</table>
% else:
<p>Sorry, no accounts found.</p>
% endif

<p class="pagelist">${currentPage.pager(format='$link_first $link_previous ~3~ $link_next $link_last:', symbol_previous='<')}</p>