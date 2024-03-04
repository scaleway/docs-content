```
terraform {
  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }
  required_version = ">= 0.13"
}
provider "scaleway" {
  access_key      = "SCW54APN8MMTF4E9HAV9"
  secret_key      = "dc7c227d-89fa-493c-a6cb-1df8f9e0b9f4"
  project_id	    = "2ea18278-847c-4c33-8111-9c2376ed921e"
  zone            = "fr-par-1"
  region          = "fr-par"
}
resource "scaleway_vpc" "vpc01" {
    name = "my-terraform-vpc"
    tags = ["demo", "terraform"]
}
resource "scaleway_vpc_private_network" "pn_priv" {
    name = "my-terraform-demo"
    tags = ["demo", "terraform"]
}
```

