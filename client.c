#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080

int client(char * hello)
{
	int status, valread, client_fd;
	struct sockaddr_in serv_addr;
	char buffer[1024] = { 0 };
	if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
		return -1;
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(PORT);


	if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)
		<= 0) {
		return -1;
	}

	if ((status
		= connect(client_fd, (struct sockaddr*)&serv_addr,
				sizeof(serv_addr)))
		< 0) {
		// printf("\nConnection Failed \n");
		return -1;
	}

	
	send(client_fd, hello, strlen(hello), 0);
	valread = read(client_fd, buffer, 1024 - 1); // subtract 1 for the null terminator at the end
	printf("%s\n\n", buffer);

	// closing the connected socket
	close(client_fd);
	return 0;
}

int main()
{
	while(1)
		client(".");
}

