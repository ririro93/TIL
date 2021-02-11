# REST API VS Soap API

## API
Application Programming Interface
- lets 2 software talk with each other

## REST
- Representational State Transfer
- 다음 규칙들을 지키면 RESTful 하다고 말할 수 있다
1. Uniform interface – Requests from different clients should look the same, for example, the same resource shouldn’t have more than one URI.
2. Client-server separation – The client and the server should act independently. They should interact with each other only through requests and responses.
3. Statelessness – There shouldn’t be any server-side sessions. Each request should contain all the information the server needs to know.
4. Cacheable resources – Server responses should contain information about whether the data they send is cacheable or not. Cacheable resources should arrive with a version number so that the client can avoid requesting the same data more than once.
5. Layered system – There might be several layers of servers between the client and the server that returns the response. This shouldn’t affect either the request or the response.
6. Code on demand [optional] – When it’s necessary, the response can contain executable code (e.g., JavaScript within an HTML response) that the client can execute.

REST 와 대응되는 SOAP에 비해 빠르고 가볍고 쉽고 데이터 중심이고 flexible하다 <br>
-> 반면에 Soap는 안전하다는 장점이 있어서 은행거래 처럼 높은 보안수준이 필요한 통신에서는 아직 쓰일 것으로 예상된다.(paypal은 Soap 쓴대)(근데 XML 밖에 못 쓴다..)

# endpoint
the touchpoint when an API interacts with another system