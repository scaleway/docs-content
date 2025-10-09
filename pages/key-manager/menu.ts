export const keyManagerMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../key-manager',
    },
    {
      label: 'Concepts',
      slug: 'concepts',
    },
    {
      label: 'Quickstart',
      slug: 'quickstart',
    },
    {
      label: 'FAQ',
      slug: 'faq',
    },
    {
      items: [
        {
          label: 'Create a Key Manager key',
          slug: 'create-km-key',
        },
        {
          label: 'Retrieve the ID of a Key Manager key',
          slug: 'retrieve-km-key-id',
        },
        {
          label:
            'Create and manage a Key Manager data encryption key',
          slug: 'create-manage-dek',
        },
        {
          label: 'Rotate Key Manager keys',
          slug: 'rotate-kem-keys',
        },
        {
          label: 'Disable Key Manager keys',
          slug: 'disable-km-keys',
        },
        {
          label: 'Schedule Key Manager keys for deletion',
          slug: 'delete-km-keys',
        },
        {
          label: 'Recover keys scheduled for deletion',
          slug: 'recover-deleted-keys',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label:
            'Understanding security measures when using Key Manager',
          slug: 'security-recommendations',
        },
        {
          label: 'Understanding Key Manager',
          slug: 'understanding-key-manager',
        },
        {
          label: 'Understanding Key Manager cryptography',
          slug: 'cryptographic-details-key-manager',
        },
        {
          label: 'Differences between Key Manager and Secret Manager',
          slug: 'differences-key-and-secret-manager',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
    {
      items: [
        {
          label: 'Key Manager API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/key-manager/',
        },
        {
          label:
            'Creating a data encryption key using the Scaleway API and the Scaleway CLI',
          slug: 'create-dek-api-cli',
        },
        {
          label: 'Setting up and configuring Tink',
          slug: 'configuring-tink',
        },
        {
          label: 'Managing your Key Manager keys using Tink',
          slug: 'manage-keys-with-tink',
        },
        {
          label: 'Rotate keys using the Scaleway CLI and API',
          slug: 'rotate-keys-api-cli',
        },
        {
          label:
            'Encrypting and decrypting data with a Key Manager data encryption key',
          slug: 'encrypt-decrypt-data-with-km-dek',
        },
        {
          label:
            'Encrypting and decrypting data streams with Streaming AEAD, Tink and Key Manager',
          slug: 'encrypt-decrypt-keys-with-streaming-aead-tink',
        },
        {
          label: 'Encrypting and decrypting data with an asymmetric key',
          slug: 'encrypt-decrypt-asymmetric-key-with-go-sdk'
        },
        {
          label: 'Managing signatures using the Scaleway Go SDK and Key Manager',
          slug: 'sign-verify-key-with-go-sdk'
        }
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
  ],
  label: 'Key Manager',
  slug: 'key-manager',
}
