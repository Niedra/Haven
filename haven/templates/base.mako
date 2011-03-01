<!DOCTYPE html>
<head>
    <title>${self.title()}</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Index</a></li>
            <li><a href="/account/list">Accounts List</a></li>
            <li><a href="/login">Login</a> - <a href="/logout">Logout</a></li>
        </ul>
    </nav>
    ${self.body()}
</body>
</html>
