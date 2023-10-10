"""
SENDING EMAILS THEORY

devices - hosts
all computers that are connected to a
network and participate directly in communication in
network are classified as hosts. Hosts can
be called endpoints

server
computers with software that allows them to provide
information, such as email or web pages, to
other end devices on the network

each service requires server software
separate. For example, a computer requires a
web server software, so you can provide
web services on the network. A computer with software
server can simultaneously provide services to many different clients

client
Software with the ability to communicate with the
server.
Example of client software and a browser
Internet. A single computer can also run
various types of client software. For example, a
user can check email and view
web page while exchanging instant messages
and listen to an audio

protocols - set of rules
In order for end devices to communicate over a network, each device
must comply with the same set of rules. These rules have many functions
in a network.

email protocols
email - method of storing, forwarding, sending and
to retrieve electronic messages over a network.
Email messages are stored in databases
data on email servers.

email client
communicate with email servers to
send and receive emails, through protocols.

Email supports three separate protocols for
Operation: SMTP, POP and IMAP. The process that sends
an email uses SMTP. A customer retrieves emails
using one of the two layer protocols
application: POP or IMAP.
"""

"""
PEER-TO-PEER
Client and server software usually run on separate computers,
but it is also possible for one computer to be used for both
functions at the same time. In small businesses and homes, you
can find computers functioning as servers and clients on the network.
This type of network is called a peer-to-peer network.

NETWORK ARCHITECTURE
For networks to function efficiently and grow, they must be built on
a standard network architecture.

There are four basic characteristics that network architects must
meet to meet user expectations:
. fault tolerance
. scalability
. quality of service (QoS)
. security

The term network architecture refers to the technologies that
support the infrastructure and programmed services and the rules,
or protocols, that move data across the network.

PROTOCOLS
In order for end devices to communicate over a network, each device must
comply with the same set of rules. These rules are called protocols and
they have many functions in a network.

URL - Universal Resource Locator
associates address with the name of the resource on the internet

URI - universal resource identifier
each identifier is unique
URL is part of the URI

HTTP
The hypertext transfer protocol, acronym HTTP. Hypertext is
structured text that uses logical connections (hyperlinks) between
us containing text. HTTP is the protocol for exchanging or
transferring hypertext. It is the basis for web data communication

An HTTP session is a sequence of request-response network
transactions. An HTTP client initiates a request by establishing a
Transmission Control Protocol (TCP) connection to a particular port
on a server (typically port 80).

An HTTP server listening on that port waits for a client request
message. Upon receiving the request, the server returns a status
line, such as "HTTP/1.1 200 OK", and its own private message.

HTTPS
Hyper text transfer protocol secure - hypertext transfer protocol
secure, is an implementation of the HTTP protocol over an additional
layer of security using the SSL/TLS protocol

TLS is especially suited to HTTP because it can provide protection
even if only one of the communicating parties is authenticated. This
is the case with HTTP transactions on the internet, where typically
only the server is authenticated.

HTTP METHODS
The HTTP protocol defines nine methods (GET, HEAD, POST, PUT, DELETE,
TRACE, OPTIONS, CONNECT and PATCH) that indicate the action to be
performed on the specified resource

The method determines what the server should do with the URL provided
when requesting a resource. An HTTP server must implement at least the
GET and HEAD methods. The GET and POST methods are the ones that appear
most commonly during web development.

GET
The GET method requests a representation of the specified resource.
Requests using GET should only retrieve data and should not have any
other effect.

POST
Sends data to be processed (for example, form data) to the specified
resource

PUT
Responsible for editing a resource

DELETE
Responsible for deleting a resource

HTTP STATUS CODE
HTTP response status codes indicate whether an HTTP request was
correctly completed. The responses are grouped into five classes:

1. Information responses (100-199)
2. Successful Answers (200-299)
3. Redirects (300-399)
4. Customer Errors (400-499)
5. Server Errors (500 - 599)

"""
