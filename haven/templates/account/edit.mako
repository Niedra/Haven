<%inherit file="../base.mako"/>
<%def name="title()">
    Haven - Edit Account
</%def>
<h1>Edit Account</h1>

<form method="POST" action="">
% for field in form:
<div>${ field.label} : ${ field } </div>

    % if field.errors:
        <ul class="errors">
            % for error in field.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

% endfor

    <input type="submit" value="Submit" />
</form>
