import dns.resolver

def get_dns_records(domain):
    try:
        # درخواست رکوردهای A برای دامنه
        result = dns.resolver.resolve(domain, 'A')  # رکورد A
        print(f"IP addresses for {domain}:")
        for ip in result:
            print(ip.to_text())
        
        # درخواست رکوردهای MX برای دامنه
        result = dns.resolver.resolve(domain, 'MX')  # رکورد MX
        print(f"\nMail Exchange servers for {domain}:")
        for mx in result:
            print(mx.exchange.to_text())

        # درخواست رکوردهای NS برای دامنه
        result = dns.resolver.resolve(domain, 'NS')  # رکورد NS
        print(f"\nName Servers for {domain}:")
        for ns in result:
            print(ns.to_text())

    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No DNS records found for {domain}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain to check DNS records (e.g., example.com): ")
    get_dns_records(domain)
