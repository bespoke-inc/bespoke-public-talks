#########################################
# Integration test with tiny models
#########################################


class TransformerLM():

    def get_perplexity(self, input, model_dir):
        # Load model
        config = GPT2Config.from_json_file(os.path.join(model_dir, 'config.bin'))
        state_dict = torch.load(os.path.join(model_dir, 'model.bin'))

        lm = GPT2LMHeadModel(config)
        lm.load_state_dict(state_dict)

        # Use model
        ...
        tokenizer(sentence, pad_to_max_length=True)
        ...
        tokenizer._pad_token
        ...
        vocab.numericalize()
        ...
        torch.no_grad()
        ...
        torch.tensor()
        ...
        lm(input_ids)
        ...
        torch.exp(loss).item()
        ...



# Run one-off, save binaries into test repo
# (Tiny, essentially-useless, one-word model)
config = GPT2Config(vocab_size=20,n_ctx=20,n_head=2,n_embd=2,n_positions=20)
gpt2_model = GPT2LMHeadModel(config=config)

torch.save(gpt2_model.state_dict(), 'test_models/model.bin')
gpt2_model.config.to_json_file('test_models/config.bin')


# The test
def test_transformers_lm(self):
    # GIVEN
    lm = TransformerLM(model_dir='test_models/')

    # WHEN
    ppl = lm.get_perplexity('test')

    # THEN we expect a valid value
    self.assertTrue(0 < ppl < 100)
